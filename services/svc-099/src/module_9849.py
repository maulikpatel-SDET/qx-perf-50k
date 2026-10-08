"""Service module 9849: business logic, no crypto."""


def calculate_total_9849(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9849():
    return 'module 9849 handles orders and invoices'
