"""Service module 27245: business logic, no crypto."""


def calculate_total_27245(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27245():
    return 'module 27245 handles orders and invoices'
