# MIT-BIH Arrhythmia Database Annotations

This file provides a description of the various annotations used in the MIT-BIH Arrhythmia Database. These annotations are critical for interpreting electrocardiogram (EKG) data.

## Beat Annotations

- `· or N`: Normal beat.
- `L`: Left bundle branch block beat.
- `R`: Right bundle branch block beat.
- `A`: Atrial premature beat.
- `a`: Aberrated atrial premature beat.
- `J`: Nodal (junctional) premature beat.
- `S`: Supraventricular premature beat.
- `V`: Premature ventricular contraction.
- `F`: Fusion of ventricular and normal beat.
- `[`: Start of ventricular flutter/fibrillation.
- `!`: Ventricular flutter wave.
- `]`: End of ventricular flutter/fibrillation.
- `e`: Atrial escape beat.
- `j`: Nodal (junctional) escape beat.
- `E`: Ventricular escape beat.
- `/`: Paced beat.
- `f`: Fusion of paced and normal beat.
- `x`: Non-conducted P-wave (blocked APB).
- `Q`: Unclassifiable beat.
- `|`: Isolated QRS-like artifact.

## Rhythm Annotations

- `(AB`: Atrial bigeminy.
- `(AFIB`: Atrial fibrillation.
- `(AFL`: Atrial flutter.
- `(B`: Ventricular bigeminy.
- `(BII`: 2° heart block.
- `(IVR`: Idioventricular rhythm.
- `(N`: Normal sinus rhythm.
- `(NOD`: Nodal (A-V junctional) rhythm.
- `(P`: Paced rhythm.
- `(PREX`: Pre-excitation (WPW).
- `(SBR`: Sinus bradycardia.
- `(SVTA`: Supraventricular tachyarrhythmia.
- `(T`: Ventricular trigeminy.
- `(VFL`: Ventricular flutter.
- `(VT`: Ventricular tachycardia.

## Signal Quality and Comment Annotations

- `qq`: Signal quality change (`c` or `n` indicates quality of upper/lower signal).
- `U`: Extreme noise or signal loss in both signals, ECG unreadable.
- `M (or MISSB)`: Missed beat.
- `P (or PSE)`: Pause.
- `T (or TS)`: Tape slippage.
