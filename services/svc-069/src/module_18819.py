"""Service module 18819: business logic, no crypto."""


def calculate_total_18819(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18819():
    return 'module 18819 handles orders and invoices'
