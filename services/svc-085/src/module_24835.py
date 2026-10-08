"""Service module 24835: business logic, no crypto."""


def calculate_total_24835(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24835():
    return 'module 24835 handles orders and invoices'
