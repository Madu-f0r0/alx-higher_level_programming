#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: a double pointer to the first node in the list
 * @number: the value in the new node created
 *
 * Return: a pointer to the new node created
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *leadNodePtr, *lagNodePtr;

	leadNodePtr = lagNodePtr = *head;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);

	newNode->n = number;
	newNode->next = NULL;

	if (*head == NULL)
	{
		*head = newNode;
	}
	else
	{
		if (newNode->n < (*head)->n)
		{
			newNode->next = *head;
			*head = newNode;
		}
		else if ((*head)->next == NULL)
		{
			(*head)->next = newNode;
		}
		else
		{
			leadNodePtr = (*head)->next;
			while(leadNodePtr)
			{
				if (newNode->n < leadNodePtr->n)
				{
					newNode->next = leadNodePtr;
					lagNodePtr->next = newNode;
					break;
				}
				else if (leadNodePtr->next == NULL)
				{
					leadNodePtr->next = newNode;
					break;
				}
				leadNodePtr = leadNodePtr->next;
				lagNodePtr = lagNodePtr->next;
			}
		}
	}
	return (newNode);
}
