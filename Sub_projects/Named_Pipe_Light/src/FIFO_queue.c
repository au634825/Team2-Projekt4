/*
 * FIFO_queue.c
 *
 *  Created on: 19 Mar 2021
 *      Author: volvofar
 */

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <limits.h>
#include <fcntl.h>
#include <unistd.h>
#include <syslog.h>
#include "errorHandling.h"

#define MAX 10
float queue_array[MAX];
int rear = -1;
int front = -1;

//This method inserts an item to your array
void FIFO(float add_item) {
	if (rear >= MAX - 1) {
		//printf("Queue Overflow \n");
		printf("Element deleted from queue is : %.0f\n", queue_array[front]);
		printf("Add item second %.0f\n", queue_array[rear]);
		front = front + 1; // items delete
		rear = rear + 1; // items add
		queue_array[rear] = add_item;

	} else {
		if (front == -1) {
			//If queue is initially empty
			front = 0;
		}
		rear = rear + 1;
		queue_array[rear] = add_item;
		printf("Add item first %.0f\n", queue_array[rear]);
	}
}
