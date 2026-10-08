"""Service module 49623: business logic, no crypto."""


def calculate_total_49623(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49623():
    return 'module 49623 handles orders and invoices'
