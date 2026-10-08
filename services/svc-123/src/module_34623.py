"""Service module 34623: business logic, no crypto."""


def calculate_total_34623(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34623():
    return 'module 34623 handles orders and invoices'
