"""Service module 21530: business logic, no crypto."""


def calculate_total_21530(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21530():
    return 'module 21530 handles orders and invoices'
