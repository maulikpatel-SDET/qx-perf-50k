"""Service module 8623: business logic, no crypto."""


def calculate_total_8623(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8623():
    return 'module 8623 handles orders and invoices'
