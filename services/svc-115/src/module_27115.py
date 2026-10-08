"""Service module 27115: business logic, no crypto."""


def calculate_total_27115(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27115():
    return 'module 27115 handles orders and invoices'
