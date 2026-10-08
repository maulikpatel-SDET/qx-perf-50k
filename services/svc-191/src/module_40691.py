"""Service module 40691: business logic, no crypto."""


def calculate_total_40691(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40691():
    return 'module 40691 handles orders and invoices'
