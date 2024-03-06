close all;
clearvars;
clc;

%% Input parameters
amplitude = 230; % [V]
sine_frequency = 50; % [Hz]
end_time = 0.1; % [s]

%% Setting up the sine
sine = @(t) amplitude * sin(t * sine_frequency);

%% Sampling and display
figure;
plot(0:1/10000:end_time, sine(0:1/10000:end_time), "b-", ...
    0:1/500:end_time, sine(0:1/500:end_time), "ro", ...
    0:1/200:end_time, sine(0:1/200:end_time), "kx");