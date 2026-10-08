"""Service module 27887: business logic, no crypto."""


def calculate_total_27887(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27887():
    return 'module 27887 handles orders and invoices'
