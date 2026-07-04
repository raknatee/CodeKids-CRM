# Class Diagram: CRM & Identity Management System

## Overview
ระบบนี้จัดการข้อมูล Lead และการติดต่อของ Codekids
โดยเชื่อมโยง Parent ↔ SocialAccount ↔ ContactSession
เพื่อ track ทุก interaction จากหลาย platform (FB/IG/Line)
และป้องกัน Duplicate Profile จากการทักหลายช่องทาง

## Diagram

```mermaid
classDiagram
    %% ==========================================
    %% ENUMERATIONS
    %% ==========================================
    class LeadStatus {
        <<enumeration>>
        NEW_LEAD
        OLD_LEAD
        OLD_CUSTOMER
    }

    class WhyCodekids {
        <<enumeration>>
        ADS
        TIKTOK
        COMMENT_RESPONSE
        WORD_OF_MOUTH
    }

    class PlatformName {
        <<enumeration>>
        FACEBOOK
        INSTAGRAM
        LINE
    }

    class Requirement {
        <<enumeration>>
        TRIAL
        CONSULT_CODING
        ONLINE_CLASS
        ENTREPRENEUR_CAMP
        TECHZANIZ_CAMP
        AI_CAMPE
        DIGITAL_ART
        BOOK
        FREE_INFORMATION
        ABOUT_CODEKIDS
        IN_HOUSE
        SUMMER_CAMPE
        OTHER
    }

    class Experience {
        <<enumeration>>
        EVER
        LITTLE
        NEVER
    }

    class Relationship {
        <<enumeration>>
        FATHER
        MOTHER
        SIBLING
        RELATIVE
    }

    class ContactType {
        <<enumeration>>
        INBOUND_ADS
        INBOUND_ORGANIC
        OUTBOUND_FOLLOWUP
    }

    %% ==========================================
    %% CORE CLASSES
    %% ==========================================
    class Parent {
        +int internal_id
        +string first_name
        +string last_name
        +string email
        +string phone
        +string district
        +string city
        +string education
        +string workplace
        +LeadStatus lead_status
        +WhyCodekids why_codekids
        +string notes
        +datetime first_contact_at
        +datetime updated_at
        
        +create() Parent
        +updateDetails(data: Object) boolean
        +linkSocialAccount(platform: PlatformName, user_id: string) void
        +addStudentRelationship(student_id: int, relationship: string) void
        +startContactSession(platform_id: int) ContactSession
    }

    class SocialAccount {
        +int platform_id
        +int internal_id
        +PlatformName platform_name
        +string platform_user_id
        
        +create() SocialAccount
        +update(data: Object) boolean
        +verifyExistence() boolean
    }

    class Student {
        +int student_id
        +string name
        +string nickname
        +Experience experience
        +datetime birthdate
        
        +create() Student
        +updateDetails(data: Object) boolean
    }

    class ParentStudent {
        <<association>>
        +int internal_id
        +int student_id
        +Relationship relationship
        
        +updateRelationship(new_relationship: relationship) boolean
    }

    class ContactSession {
        +int session_id
        +int internal_id
        +int platform_id
        +datetime contacted_at
        +datetime admin_responded_at
        +string followup_tag
        +Requirement requirement
        +ContactType contact_type
        +string insight
        +string session_notes
        +datetime updated_at
        
        +create() ContactSession
        +updateDetails(data: Object) boolean
        +markAdminResponded(timestamp: datetime) void
        +attachAdsInteraction(ads_id: string, platform: string) void
    }

    class AdsInteraction {
        +int ads_interaction_id
        +int session_id
        +string ads_id
        +string platform_name
        
        +create() AdsInteraction
    }

    %% ==========================================
    %% RELATIONSHIPS
    %% ==========================================
    Parent "1" -- "*" SocialAccount : has
    Parent "1" -- "*" ParentStudent : relates
    Student "1" -- "*" ParentStudent : relates
    Parent "1" -- "*" ContactSession : initiates
    SocialAccount "1" -- "*" ContactSession : used_in
    ContactSession "1" *-- "*" AdsInteraction : contains

```

## Notes

### `ContactSession.followup_tag`

**Type** `string` (free-text) 
**เขียนโดย**  Sale Admin 
**วัตถุประสงค์** ระบุลำดับหรือสถานะการติดตามผล
**ตัวอย่าง** `"1st follow-up"`, `"2nd follow-up"`
 
> ออกแบบมาเพื่อรองรับกระบวนการทำงานเดิมจาก Excel ที่ต้องนับครั้งการทักซ้ำ

---

### `ContactSession.insight`
**Type** `string` (free-text) 
**เขียนโดย**  Sale Admin 
**วัตถุประสงค์** บันทึกข้อวิเคราะห์เชิงลึกที่ได้จากการพูดคุย
**ตัวอย่าง** บริบทของครอบครัว, พฤติกรรมของเด็ก, โอกาสในการปิดการขาย

---

### `ContactSession.session_notes`
**Type** `string` (free-text) 
**เขียนโดย**  Data Entry Admin 
**วัตถุประสงค์**  Log การพูดคุย หรือข้อความดิบที่ลูกค้าส่งมาในแชต
 
> Fallback field สำหรับข้อมูลที่ระบบยังไม่มีฟิลด์เฉพาะรองรับ เพื่อป้องกันข้อมูลสูญหาย

---

### `Parent.startContactSession(platform_id)`
**Input** `platform_id: int`
**Output** `ContactSession`
**วัตถุประสงค์** เปิด Ticket สนทนาใหม่ พร้อมระบุว่าลูกค้าติดต่อผ่าน Social Account ตัวไหน
 
> จำเป็นต้องส่ง `platform_id` เพื่อให้ระบบ track ได้ว่า session นี้มาจาก Line, Facebook หรือ Instagram

---

### `SocialAccount.verifyExistence()`
**Output** `boolean`
**ตรวจสอบกับ** Database ภายใน (ไม่ใช่ platform API)
**วัตถุประสงค์** เช็คว่า `platform_user_id` นี้มีอยู่ในระบบแล้วหรือยัง

> หากพบแล้ว ระบบจะดึง `internal_id` เดิมมาใช้แทนการสร้าง Parent ใหม่ เพื่อป้องกัน Duplicate Profile

---

### `ContactSession.attachAdsInteraction(ads_id, platform)`
**Input** `ads_id: string`, `platform: string`
**วัตถุประสงค์** สร้าง Record ใน `AdsInteraction` ผูกกับ Session นี้
**ที่มาของ ads_id** Admin กรอกเอง หรือจากระบบ OCR สแกนภาพ
 
> ใช้สำหรับทำ Attribution และคำนวณ ROI ทางการตลาด