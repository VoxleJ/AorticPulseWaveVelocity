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
