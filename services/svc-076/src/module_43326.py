"""Service module 43326: business logic, no crypto."""


def calculate_total_43326(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43326():
    return 'module 43326 handles orders and invoices'
