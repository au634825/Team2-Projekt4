################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/FIFO_queue.c \
../src/NamedPipeCommunication.c \
../src/Named_Pipe_Temp.c \
../src/errorHandling.c \
../src/temperature.c \
../src/try-catch.c 

OBJS += \
./src/FIFO_queue.o \
./src/NamedPipeCommunication.o \
./src/Named_Pipe_Temp.o \
./src/errorHandling.o \
./src/temperature.o \
./src/try-catch.o 

C_DEPS += \
./src/FIFO_queue.d \
./src/NamedPipeCommunication.d \
./src/Named_Pipe_Temp.d \
./src/errorHandling.d \
./src/temperature.d \
./src/try-catch.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Cross GCC Compiler'
	arm-linux-gnueabihf-gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


