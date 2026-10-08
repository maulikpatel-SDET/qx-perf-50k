"""Service module 27808: business logic, no crypto."""


def calculate_total_27808(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27808():
    return 'module 27808 handles orders and invoices'
