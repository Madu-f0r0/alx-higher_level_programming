#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: a pointer to the first node of the list in question
 *
 * Return: 1 if a cycle is detected; 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *nodePtr, *head;

	head = nodePtr = list;
	while (nodePtr)
	{
		nodePtr = list->next;
		list = nodePtr;

		if (nodePtr == head)
		{
			return (1);
		}
	}
	return (0);
}
