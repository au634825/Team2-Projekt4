################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/FIFO_queue.c \
../src/LUXSensor.c \
../src/NamedPipeCommunication.c \
../src/Named_Pipe_Light.c \
../src/errorHandling.c \
../src/gpio.c 

OBJS += \
./src/FIFO_queue.o \
./src/LUXSensor.o \
./src/NamedPipeCommunication.o \
./src/Named_Pipe_Light.o \
./src/errorHandling.o \
./src/gpio.o 

C_DEPS += \
./src/FIFO_queue.d \
./src/LUXSensor.d \
./src/NamedPipeCommunication.d \
./src/Named_Pipe_Light.d \
./src/errorHandling.d \
./src/gpio.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Cross GCC Compiler'
	arm-linux-gnueabihf-gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


