[![Build Status](https://travis-ci.org/VoxleJ/AorticPulseWaveVelocity.svg?branch=master)](https://travis-ci.org/VoxleJ/AorticPulseWaveVelocity)
# Aortic Pulse Wave Velocity and Transit Time Analysis 

This is a project focused on calculating Aortic Pulse Wave velocity given flow velocity waveforms. This contains/will contain 2 major components.

  - Transit Time Algorithms
  - Full Pulse Wave Velocity Calculations

### Transit Time Analysis

  - The goal is to have a few different algorithms, XCorr, TTPoint (or more notably known as half max) and Group Delay in order to test for accuracy
  - Can be used for flow or velocity waveforms, however all testing has been done with flow-time plots
  - There is a possibility to expand these and add more algorithms, however XCorr and TTPoint 50% should be sufficient and is now available in the script TransitTimeEstimator.py

### Pulse Wave Velocity
  - This requires an external input of aortic arch/aortic length
  - Aortic Arch length was measured using a 3D centreline and then PWV was calculated externally.

# So What is Going on Now? 

### Dec. 13, 2019
  -After working on the script on and off, it came to a deadline of a week and a half to finish the script. TT50 (half max), TT20/25 all work after some minor adjustments.
  - A main issue was a trigger time issue that moved the foot/upslope times of the flow waveform to a distant time point. To combat this I circularly shifted all of the flow waveforms relative to where the foot time was most plausible to be. After the shift I then interpolated the waveforms and that sped up the XCorr method.
  -I will continue to work on this and add more methods, but as of now the script is stable.

### Oct. 2, 2019
  - I added TT50, 25 and 20 to the main script. A user will now be prompted to enter which foot to foot method they would like to use.
  - I have also added a quick 3D Checking Script. This is to check how well the 3D centerline is traced in the Aortic Arch.

### Sept. 27, 2019
  - I still have some issues with the XCorr method, however I was missing a crucial step: I needed to normalize my data. After normalizing my data I'm getting much better values. However, normalizing has made this much more expensive. I am considering changing the interoplation method/number of points. Depending on the dataset I could have 1293000 points, therefore making the xcorr take way too long. 
  - Currently I am having a difficult time with TT50 and TT25, theoretically all the method needs to do is get 50% or 25% of the max upslope, and get the distance/subtract. Now this should give the Transit Time, but it doesn't. 
