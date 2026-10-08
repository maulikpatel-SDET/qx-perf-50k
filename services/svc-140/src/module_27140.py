"""Service module 27140: business logic, no crypto."""


def calculate_total_27140(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27140():
    return 'module 27140 handles orders and invoices'
