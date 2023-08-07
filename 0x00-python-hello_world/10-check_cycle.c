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
		if (nodePtr->next == head)
		{
			return (1);
		}

		nodePtr = list->next;
		list = nodePtr;
	}
	return (0);
}
