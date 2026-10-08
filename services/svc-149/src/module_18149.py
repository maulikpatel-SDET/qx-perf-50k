"""Service module 18149: business logic, no crypto."""


def calculate_total_18149(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18149():
    return 'module 18149 handles orders and invoices'
