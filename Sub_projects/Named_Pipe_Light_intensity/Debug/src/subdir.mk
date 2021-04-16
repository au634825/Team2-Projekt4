################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/Named_Pipe_Light_intensity.c \
../src/lysintensitet.c \
../src/pin_data.c \
../src/setitimer.c \
../src/sig_handler.c 

OBJS += \
./src/Named_Pipe_Light_intensity.o \
./src/lysintensitet.o \
./src/pin_data.o \
./src/setitimer.o \
./src/sig_handler.o 

C_DEPS += \
./src/Named_Pipe_Light_intensity.d \
./src/lysintensitet.d \
./src/pin_data.d \
./src/setitimer.d \
./src/sig_handler.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Cross GCC Compiler'
	arm-linux-gnueabihf-gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


