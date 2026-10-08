"""Service module 26191: business logic, no crypto."""


def calculate_total_26191(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26191():
    return 'module 26191 handles orders and invoices'
