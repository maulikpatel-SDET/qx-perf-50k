"""Service module 21538: business logic, no crypto."""


def calculate_total_21538(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21538():
    return 'module 21538 handles orders and invoices'
