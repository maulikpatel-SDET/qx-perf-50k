"""Service module 28385: business logic, no crypto."""


def calculate_total_28385(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28385():
    return 'module 28385 handles orders and invoices'
