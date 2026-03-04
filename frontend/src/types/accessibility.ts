/** Accessibility Types */

export type FontFamily = 'system' | 'OpenDyslexic' | 'Arial' | 'Georgia' | 'Verdana' | 'Trebuchet';
export type ColorOverlay = 'none' | 'blue' | 'green' | 'yellow' | 'sepia';
export type ReadingLevel = 'basic' | 'intermediate' | 'advanced';

export interface AccessibilitySettings {
  fontSize: number;
  lineSpacing: number;
  letterSpacing: number;
  fontFamily: FontFamily;
  colorOverlay: ColorOverlay;
  highContrastMode: boolean;
  darkMode: boolean;
  simplifyText: boolean;
  readingLevel: ReadingLevel;
  speechRate: number;
  reduceMotion: boolean;
  reduceAnimation: boolean;
  soundEnabled: boolean;
  vibrationEnabled: boolean;
  minimalMode: boolean;
  guidedMode: boolean;
  showAvatar: boolean;
}

export interface User {
  id: number;
  email: string;
  full_name?: string;
  created_at: string;
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
}

export interface TextSimplifyRequest {
  text: string;
  reading_level: ReadingLevel;
}

export interface TextSimplifyResponse {
  original_text: string;
  simplified_text: string;
  reading_level: ReadingLevel;
}
