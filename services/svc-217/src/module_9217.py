"""Service module 9217: business logic, no crypto."""


def calculate_total_9217(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9217():
    return 'module 9217 handles orders and invoices'
