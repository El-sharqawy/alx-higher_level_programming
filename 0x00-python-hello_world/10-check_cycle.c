#include "lists.h"

/**
 * check_cycle - check if the list has a cycle
 * @head: pointer to list to be checked
 * Return: void
*/
int check_cycle(listint_t *head)
{
	listint_t *newHead = head;
	listint_t *next = head->next;

	if (head == NULL || head->next == NULL)
		return (0);

	if (newHead->next == NULL || next == NULL || next->next == NULL)
		return (0);

	while (next != NULL && next->next != NULL)
	{
		if (newHead == next)
			return (1);
		newHead = newHead->next;
		next = next->next->next;
	}
	return (0);
}
