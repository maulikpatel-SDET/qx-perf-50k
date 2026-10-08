"""Service module 24041: business logic, no crypto."""


def calculate_total_24041(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24041():
    return 'module 24041 handles orders and invoices'
