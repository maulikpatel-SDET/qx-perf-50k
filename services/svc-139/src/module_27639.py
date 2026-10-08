"""Service module 27639: business logic, no crypto."""


def calculate_total_27639(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27639():
    return 'module 27639 handles orders and invoices'
