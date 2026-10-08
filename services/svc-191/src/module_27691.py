"""Service module 27691: business logic, no crypto."""


def calculate_total_27691(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27691():
    return 'module 27691 handles orders and invoices'
