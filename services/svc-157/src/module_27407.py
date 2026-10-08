"""Service module 27407: business logic, no crypto."""


def calculate_total_27407(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27407():
    return 'module 27407 handles orders and invoices'
