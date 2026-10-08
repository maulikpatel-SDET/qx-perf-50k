"""Service module 27598: business logic, no crypto."""


def calculate_total_27598(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27598():
    return 'module 27598 handles orders and invoices'
