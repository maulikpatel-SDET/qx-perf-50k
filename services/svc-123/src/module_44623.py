"""Service module 44623: business logic, no crypto."""


def calculate_total_44623(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44623():
    return 'module 44623 handles orders and invoices'
