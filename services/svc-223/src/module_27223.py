"""Service module 27223: business logic, no crypto."""


def calculate_total_27223(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27223():
    return 'module 27223 handles orders and invoices'
