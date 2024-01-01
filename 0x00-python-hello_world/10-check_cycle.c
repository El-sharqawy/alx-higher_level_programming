#include "lists.h"

/**
 * check_cycle - check if the list has a cycle
 * @head: pointer to list to be checked
 * Return: void
*/
int check_cycle(listint_t *head)
{
	listint_t *newHead = head;
	listint_t *next = head;

	if (!head)
		return (0);

	while (newHead && next && next->next)
	{
		newHead = newHead->next;
		next = next->next->next;
		if (newHead == next)
			return (1);
	}
	return (0);
}
