/**
 * Sign Language Avatar Component
 * Display sign language interpretation of text for deaf/hard of hearing users
 */

import React, { useState, useEffect } from 'react';
import axios from 'axios';

interface Animation {
  word: string;
  video?: string;
  letters?: string[];
  type?: string;
  duration: number;
  recognized: boolean;
}

interface AvatarData {
  text: string;
  word_count: number;
  recognized_words: number;
  unrecognized_words: string[];
  total_duration_seconds: number;
  animation_data: {
    animations: Animation[];
  };
  avatar_speed: string;
}

interface SignLanguageAvatarProps {
  text: string;
  onComplete?: () => void;
  isVisible: boolean;
}

export const SignLanguageAvatar: React.FC<SignLanguageAvatarProps> = ({
  text,
  onComplete,
  isVisible,
}) => {
  const [loading, setLoading] = useState(false);
  const [avatarData, setAvatarData] = useState<AvatarData | null>(null);
  const [currentWordIndex, setCurrentWordIndex] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (text && isVisible) {
      generateAvatarAnimation();
    }
  }, [text, isVisible]);

  const generateAvatarAnimation = async () => {
    if (!text.trim()) {
      setError('Please provide text for sign language interpretation');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await axios.post('/api/v1/avatar/sign', {
        text: text,
      });
      setAvatarData(response.data.avatar_data);
      setCurrentWordIndex(0);
    } catch (err) {
      setError('Failed to generate sign language animation. Please try again.');
      console.error('Avatar generation error:', err);
    } finally {
      setLoading(false);
    }
  };

  const playAnimation = () => {
    if (!avatarData) return;

    setIsPlaying(true);
    let index = 0;

    const playNextWord = () => {
      if (index < avatarData.animation_data.animations.length) {
        setCurrentWordIndex(index);
        const animation = avatarData.animation_data.animations[index];

        setTimeout(() => {
          index++;
          playNextWord();
        }, animation.duration);
      } else {
        setIsPlaying(false);
        if (onComplete) {
          onComplete();
        }
      }
    };

    playNextWord();
  };

  const pauseAnimation = () => {
    setIsPlaying(false);
  };

  const resetAnimation = () => {
    setCurrentWordIndex(0);
    setIsPlaying(false);
  };

  if (!isVisible) {
    return null;
  }

  return (
    <div
      className="sign-language-avatar"
      role="region"
      aria-label="Sign language avatar interpretation"
    >
      <h3>Sign Language Interpretation (ASL)</h3>

      {error && (
        <div className="error-message" role="alert">
          {error}
        </div>
      )}

      {loading && (
        <div className="loading">
          <p>Generating sign language animation...</p>
        </div>
      )}

      {avatarData && !loading && (
        <div className="avatar-container">
          {/* Avatar Display Area */}
          <div className="avatar-display">
            <div className="avatar-placeholder">
              <svg
                viewBox="0 0 200 300"
                className="avatar-figure"
                aria-label={`Avatar showing sign for: ${avatarData.animation_data.animations[currentWordIndex]?.word}`}
              >
                {/* Simple avatar representation */}
                <circle cx="100" cy="50" r="30" fill="#8B4513" /> {/* Head */}
                <rect x="85" y="85" width="30" height="60" fill="#FFB6C1" /> {/* Body */}
                <line x1="100" y1="145" x2="80" y2="200" stroke="#FFB6C1" strokeWidth="8" /> {/* Left leg */}
                <line x1="100" y1="145" x2="120" y2="200" stroke="#FFB6C1" strokeWidth="8" /> {/* Right leg */}
                {/* Hands will animate based on word */}
                <circle cx="70" cy="100" r="12" fill="#FFB6C1" /> {/* Left hand */}
                <circle cx="130" cy="100" r="12" fill="#FFB6C1" /> {/* Right hand */}
              </svg>
            </div>

            {/* Current Word Display */}
            <div className="current-word">
              {currentWordIndex < avatarData.animation_data.animations.length && (
                <div>
                  <p className="word-label">Now signing:</p>
                  <p className="word-text">
                    {avatarData.animation_data.animations[currentWordIndex].word}
                  </p>
                </div>
              )}
            </div>
          </div>

          {/* Controls */}
          <div className="avatar-controls">
            <button
              onClick={playAnimation}
              disabled={isPlaying}
              aria-label="Play sign language animation"
            >
              ▶ Play
            </button>
            <button
              onClick={pauseAnimation}
              disabled={!isPlaying}
              aria-label="Pause animation"
            >
              ⏸ Pause
            </button>
            <button
              onClick={resetAnimation}
              aria-label="Reset animation to beginning"
            >
              ↻ Reset
            </button>
          </div>

          {/* Progress */}
          <div className="avatar-progress">
            <div className="progress-bar">
              <div
                className="progress-fill"
                style={{
                  width: `${(currentWordIndex / avatarData.animation_data.animations.length) * 100}%`,
                }}
              />
            </div>
            <p className="progress-text">
              {currentWordIndex + 1} of {avatarData.animation_data.animations.length} words
            </p>
          </div>

          {/* Word List */}
          <div className="word-list">
            <h4>Word by word:</h4>
            <div className="words-container">
              {avatarData.animation_data.animations.map((animation, index) => (
                <button
                  key={index}
                  className={`word-chip ${index === currentWordIndex ? 'active' : ''} ${animation.recognized ? 'recognized' : 'fingerspelled'}`}
                  onClick={() => setCurrentWordIndex(index)}
                  title={animation.recognized ? 'Recognized sign' : 'Fingerspelled'}
                >
                  {animation.word}
                </button>
              ))}
            </div>
          </div>

          {/* Statistics */}
          <div className="avatar-stats">
            <p>
              <strong>Recognized signs:</strong> {avatarData.recognized_words} /{' '}
              {avatarData.word_count}
            </p>
            <p>
              <strong>Duration:</strong> {avatarData.total_duration_seconds.toFixed(1)} seconds
            </p>
          </div>
        </div>
      )}

      <style>{`
        .sign-language-avatar {
          background: #f5f5f5;
          border: 2px solid #ddd;
          border-radius: 8px;
          padding: 20px;
          margin: 20px 0;
        }

        .avatar-container {
          display: flex;
          flex-direction: column;
          align-items: center;
          gap: 20px;
        }

        .avatar-display {
          display: flex;
          gap: 20px;
          align-items: center;
          width: 100%;
          justify-content: center;
          flex-wrap: wrap;
        }

        .avatar-placeholder {
          background: white;
          border: 2px solid #ccc;
          border-radius: 8px;
          padding: 20px;
          width: 200px;
          height: 300px;
          display: flex;
          align-items: center;
          justify-content: center;
        }

        .avatar-figure {
          width: 100%;
          height: 100%;
        }

        .current-word {
          text-align: center;
          min-height: 80px;
          display: flex;
          align-items: center;
          justify-content: center;
        }

        .word-label {
          font-size: 12px;
          color: #666;
          margin: 0;
        }

        .word-text {
          font-size: 28px;
          font-weight: bold;
          margin: 10px 0 0 0;
          color: #333;
        }

        .avatar-controls {
          display: flex;
          gap: 10px;
          justify-content: center;
          flex-wrap: wrap;
        }

        .avatar-controls button {
          padding: 10px 20px;
          background: #0066cc;
          color: white;
          border: none;
          border-radius: 4px;
          cursor: pointer;
          font-size: 14px;
        }

        .avatar-controls button:disabled {
          background: #ccc;
          cursor: not-allowed;
        }

        .avatar-controls button:hover:not(:disabled) {
          background: #0052a3;
        }

        .avatar-progress {
          width: 100%;
          max-width: 400px;
        }

        .progress-bar {
          height: 8px;
          background: #ddd;
          border-radius: 4px;
          overflow: hidden;
        }

        .progress-fill {
          height: 100%;
          background: #4CAF50;
          transition: width 0.3s ease;
        }

        .progress-text {
          font-size: 12px;
          color: #666;
          margin-top: 8px;
          text-align: center;
        }

        .word-list {
          width: 100%;
        }

        .word-list h4 {
          margin: 0 0 10px 0;
          font-size: 14px;
        }

        .words-container {
          display: flex;
          flex-wrap: wrap;
          gap: 8px;
          justify-content: center;
        }

        .word-chip {
          padding: 6px 12px;
          background: #f0f0f0;
          border: 1px solid #ccc;
          border-radius: 20px;
          cursor: pointer;
          font-size: 12px;
          transition: all 0.2s;
        }

        .word-chip.recognized {
          border-color: #4CAF50;
        }

        .word-chip.fingerspelled {
          border-color: #FF9800;
        }

        .word-chip.active {
          background: #0066cc;
          color: white;
          border-color: #0066cc;
        }

        .word-chip:hover {
          transform: scale(1.05);
        }

        .avatar-stats {
          width: 100%;
          padding: 10px;
          background: white;
          border-radius: 4px;
          font-size: 12px;
          color: #666;
        }

        .avatar-stats p {
          margin: 5px 0;
        }

        .error-message {
          color: #d32f2f;
          background: #ffebee;
          padding: 10px;
          border-radius: 4px;
          margin-bottom: 10px;
        }

        .loading {
          text-align: center;
          padding: 20px;
          color: #0066cc;
        }
      `}</style>
    </div>
  );
};

export default SignLanguageAvatar;
