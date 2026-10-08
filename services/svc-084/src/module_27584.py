"""Service module 27584: business logic, no crypto."""


def calculate_total_27584(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27584():
    return 'module 27584 handles orders and invoices'
