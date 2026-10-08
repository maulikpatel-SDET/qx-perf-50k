"""Service module 27883: business logic, no crypto."""


def calculate_total_27883(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27883():
    return 'module 27883 handles orders and invoices'
