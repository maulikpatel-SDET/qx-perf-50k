"""Service module 7307: business logic, no crypto."""


def calculate_total_7307(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7307():
    return 'module 7307 handles orders and invoices'
