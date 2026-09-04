export interface TeachingDetails {
  teacherName: string;
  teacherId: string;
  course: string;
  classId: string;
  sessionNumber: string;
  studentName: string;
  studentId: string;
  paymentDate: string | null;
}

export interface StudentFeedback {
  engagementScore: number | null;
  learnings: string;
  portfolioLink: string;
  captureFile: File | null;
}

export interface SelfFeedback {
  engagementScore: number | null;
}