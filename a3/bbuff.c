#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <semaphore.h>
#include "bbuff.h"

// Prototype Declaration
void bbuff_init(void);
void bbuff_blocking_insert(void* item);
void* bbuff_blocking_extract(void);
_Bool bbuff_is_empty(void);

static void* bbuff[BUFFER_SIZE];
sem_t mutex;
sem_t num_items;
sem_t empty_slots;

void bbuff_init(void)
{
	for (int i = 0; i < BUFFER_SIZE; ++i)
	{
		bbuff[i] = NULL;
	}
	sem_init(&mutex, 0, 1);
	sem_init(&num_items, 0, 0);
	sem_init(&empty_slots, 0, BUFFER_SIZE);
}

void bbuff_blocking_insert(void* item)
{
	
	sem_wait(&empty_slots);
	sem_wait(&mutex);
	// int i = 0;
	// while(bbuff[i] != NULL) i++;
	// bbuff[i] = item;
	// printf("Insert i = %d\n", i);
	int tail;
	sem_getvalue(&num_items, &tail);
	bbuff[tail] = item;
	sem_post(&mutex);
	sem_post(&num_items);
	
}

void* bbuff_blocking_extract(void)
{
	
	sem_wait(&num_items);
	sem_wait(&mutex);
	// int i = 0;
	// while(bbuff[i] == NULL && !bbuff_is_empty()) i++;
	// printf("Extract i = %d\n", i);
	// void *temp = malloc(sizeof(void*));
	// if (temp == NULL)
	// {
	// 	printf("Error: Could not allocate in func bbuff_blocking_extract().\n");
	// 	exit(-1);
	// }
	// memcpy(bbuff[i], temp, sizeof(void*));
	// bbuff[i] = NULL;
	// printf("Error may be here\n");
	int tail;
	sem_getvalue(&num_items, &tail);
	void *temp = malloc(sizeof(void*));
	memcpy(bbuff[tail], temp, sizeof(void*));
	bbuff[tail] = NULL;
	sem_post(&mutex);
	sem_post(&empty_slots);
	return temp;
	
}

_Bool bbuff_is_empty(void)
{
	int sem_val;
	sem_getvalue(&num_items, &sem_val);
	return sem_val == 0;
}