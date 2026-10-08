"""Service module 27188: business logic, no crypto."""


def calculate_total_27188(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27188():
    return 'module 27188 handles orders and invoices'
