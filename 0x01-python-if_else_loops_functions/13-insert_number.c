#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to head of list
 * @number: integer to be inserted in node
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode;
	listint_t *curr;
	listint_t *prev;

	newNode = malloc(sizeof(listint_t));

	if (!newNode)
		return (NULL);

	newNode->n = number;
	newNode->next = NULL;

	curr = *head;
	prev = NULL;

	while (curr && curr->n < number)
	{
		prev = curr;
		curr = curr->next;
	}

	if (!prev)
	{
		newNode->next = *head;
		*head = newNode;
	}
	else
	{
		prev->next = newNode;
		newNode->next = curr;
	}

	return (newNode);
}
