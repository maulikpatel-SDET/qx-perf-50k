"""Service module 27705: business logic, no crypto."""


def calculate_total_27705(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27705():
    return 'module 27705 handles orders and invoices'
