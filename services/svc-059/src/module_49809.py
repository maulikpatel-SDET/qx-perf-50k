"""Service module 49809: business logic, no crypto."""


def calculate_total_49809(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49809():
    return 'module 49809 handles orders and invoices'
