"""Service module 43550: business logic, no crypto."""


def calculate_total_43550(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43550():
    return 'module 43550 handles orders and invoices'
