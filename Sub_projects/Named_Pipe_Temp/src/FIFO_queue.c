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
		printf("Element deleted from queue is : %.2f\n", queue_array[front]);
		printf("Add item second %.2f\n", queue_array[rear]);
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
		printf("Add item first %.2f\n", queue_array[rear]);
	}
}

////This method inserts an item to your array
//void insert() {
//	int add_item;
//	if (rear == MAX - 1) {
//		printf("Queue Overflow \n");
//	} else {
//		if (front == -1) {
//			//If queue is initially empty
//			front = 0;
//		}
//		printf("Inset the element in queue : ");
//		scanf("%d", &add_item);
//		rear = rear + 1;
//		queue_array[rear] = add_item;
//	}
//}
//
//void delete() {
//	if (front == -1 || front > rear) {
//		printf("Queue Underflow \n");
//	} else {
//		printf("Element deleted from queue is : %d\n", queue_array[front]);
//		front = front + 1;
//	}
//}

//// A structure to represent a queue
//struct Queue {
//	int front, rear, size;
//	unsigned capacity;
//	int *array;
//};
//
//// function to create a queue
//// of given capacity.
//// It initializes size of queue as 0
//struct Queue* createQueue(unsigned capacity) {
//	struct Queue *queue = (struct Queue*) malloc(sizeof(struct Queue));
//	queue->capacity = capacity;
//	queue->front = queue->size = 0;
//
//	// This is important, see the enqueue
//	queue->rear = capacity - 1;
//	queue->array = (int*) malloc(queue->capacity * sizeof(int));
//	return queue;
//}
//// Queue is full when size becomes
//// equal to the capacity
//int isFull(struct Queue *queue) {
//	return (queue->size == queue->capacity);
//}
//
//// Queue is empty when size is 0
//int isEmpty(struct Queue *queue) {
//	return (queue->size == 0);
//}
//
//// Function to add an item to the queue.
//// It changes rear and size
//void enqueue(struct Queue *queue, int item) {
//	if (isFull(queue))
//		return;
//	queue->rear = (queue->rear + 1) % queue->capacity;
//	queue->array[queue->rear] = item;
//	queue->size = queue->size + 1;
//	printf("%d enqueued to queue\n", item);
//}
//
//// Function to remove an item from queue.
//// It changes front and size
//int dequeue(struct Queue *queue) {
//	if (isEmpty(queue))
//		return INT_MIN;
//	int item = queue->array[queue->front];
//	queue->front = (queue->front + 1) % queue->capacity;
//	queue->size = queue->size - 1;
//	return item;
//}
//
//// Function to get front of queue
//int front(struct Queue *queue) {
//	if (isEmpty(queue))
//		return INT_MIN;
//	return queue->array[queue->front];
//}
//
//// Function to get rear of queue
//int rear(struct Queue *queue) {
//	if (isEmpty(queue))
//		return INT_MIN;
//	return queue->array[queue->rear];
//}
