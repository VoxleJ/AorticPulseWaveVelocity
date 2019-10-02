[![Build Status](https://travis-ci.org/VoxleJ/AorticPulseWaveVelocity.svg?branch=master)](https://travis-ci.org/VoxleJ/AorticPulseWaveVelocity)
# Aortic Pulse Wave Velocity and Transit Time Analysis 

This is a project focused on calculating Aortic Pulse Wave velocity given flow velocity waveforms. This contains/will contain 2 major components.

  - Transit Time Algorithms
  - Full Pulse Wave Velocity Calculations

### Transit Time Analysis

  - The goal is to have a few different algorithms, XCorr, TT50, TT25 and Group Delay in order to test for accuracy
  - Can be used for flow or velocity waveforms, however all testing has been done with flow-time plots
  - There is a possibility to expand these and add more algorithms, however XCorr and TT50/25 should be sufficient

### Pulse Wave Velocity
  - This requires an external input of aortic arch/aortic length
  - For this project I measured full aortic and aortic arch length using a 3D centerline

# So What is Going on Now? 

### Oct. 2, 2019
  - I added TT50, 25 and 20 to the main script. A user will now be prompted to enter which foot to foot method they would like to use.

### Sept. 27, 2019
  - I still have some issues with the XCorr method, however I was missing a crucial step: I needed to normalize my data. After normalizing my data I'm getting much better values. However, normalizing has made this much more expensive. I am considering changing the interoplation method/number of points. Depending on the dataset I could have 1293000 points, therefore making the xcorr take way too long. 
  - Currently I am having a difficult time with TT50 and TT25, theoretically all the method needs to do is get 50% or 25% of the max    upslope, and get the distance/subtract. Now this should give the Transit Time, but it doesn't.  
  - I have not worked on the group delay method.
